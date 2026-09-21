/**
 * Cloudflare Pages / Worker Function: /api/contact
 * Handles contact / consultation requests and sends inquiries to Kelly.
 */
export async function onRequestPost(context) {
  const { request, env } = context;

  try {
    const data = await request.json();
    const name = data.name ? String(data.name).trim() : '';
    const email = data.email ? String(data.email).trim() : '';
    const phone = data.phone ? String(data.phone).trim() : '';
    const preference = data.preference || 'Not specified';
    const message = data.message ? String(data.message).trim() : '';
    const timestamp = data.timestamp || new Date().toISOString();

    if (!name || !email || !message) {
      return new Response(JSON.stringify({ error: 'Name, email, and message are required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    console.log(`[CONTACT_INQUIRY] from: ${name} <${email}>, phone: ${phone}, pref: ${preference}`);

    // 1. If KV is bound, store a copy of the inquiry
    if (env && env.INQUIRIES) {
      await env.INQUIRIES.put(`inquiry:${Date.now()}:${email}`, JSON.stringify({
        name, email, phone, preference, message, timestamp
      }));
    } else if (env && env.GTC_DATA) {
      await env.GTC_DATA.put(`inquiry:${Date.now()}:${email}`, JSON.stringify({
        name, email, phone, preference, message, timestamp
      }));
    }

    // 2. If a webhook (Zapier, Slack, Discord, Google Sheets, Make) or email service is configured
    if (env && env.CONTACT_WEBHOOK_URL) {
      try {
        await fetch(env.CONTACT_WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            name, email, phone, preference, message, timestamp,
            recipient: 'goodtherapycolorado@gmail.com'
          })
        });
      } catch (webhookErr) {
        console.error('Webhook error:', webhookErr);
      }
    }

    // 3. If Resend / Postmark API key is present in env (e.g. env.RESEND_API_KEY)
    if (env && env.RESEND_API_KEY) {
      try {
        await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${env.RESEND_API_KEY}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            from: 'Good Therapy Website <website@goodtherapycolorado.com>',
            to: ['goodtherapycolorado@gmail.com'],
            reply_to: email,
            subject: `New Therapy Inquiry from ${name}`,
            text: `Name: ${name}\nEmail: ${email}\nPhone: ${phone}\nPreferred Appointment: ${preference}\n\nMessage:\n${message}`
          })
        });
      } catch (resendErr) {
        console.error('Resend error:', resendErr);
      }
    }

    return new Response(JSON.stringify({
      success: true,
      message: 'Inquiry received successfully. Kelly will be in touch shortly!'
    }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });
  } catch (err) {
    console.error('Contact error:', err);
    return new Response(JSON.stringify({ error: 'Internal server error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    }
  });
}
