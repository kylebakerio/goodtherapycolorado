/**
 * Cloudflare Worker router for Good Therapy Colorado.
 * Serves static assets and provides API handlers for /api/subscribe and /api/contact.
 */

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // 1. CORS Preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        status: 204,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type'
        }
      });
    }

    // 2. Newsletter / Mailing List API
    if (url.pathname === '/api/subscribe' && request.method === 'POST') {
      try {
        const data = await request.json();
        const email = data.email ? String(data.email).trim() : '';

        if (!email || !email.includes('@')) {
          return Response.json({ error: 'Valid email is required' }, { status: 400 });
        }

        const timestamp = data.timestamp || new Date().toISOString();
        console.log(`[SUBSCRIBER] ${email} at ${timestamp}`);

        if (env.SUBSCRIBERS) {
          await env.SUBSCRIBERS.put(`sub:${Date.now()}:${email}`, JSON.stringify({ email, timestamp }));
        } else if (env.GTC_DATA) {
          await env.GTC_DATA.put(`sub:${Date.now()}:${email}`, JSON.stringify({ email, timestamp }));
        }

        if (env.NEWSLETTER_WEBHOOK_URL) {
          try {
            await fetch(env.NEWSLETTER_WEBHOOK_URL, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ email, timestamp })
            });
          } catch(e) {}
        }

        return Response.json({ success: true, message: 'Subscribed successfully' });
      } catch (err) {
        return Response.json({ error: 'Failed to process subscription' }, { status: 500 });
      }
    }

    // 3. Contact Form API
    if (url.pathname === '/api/contact' && request.method === 'POST') {
      try {
        const data = await request.json();
        const { name, email, phone, preference, message } = data;

        if (!name || !email || !message) {
          return Response.json({ error: 'Name, email, and message are required' }, { status: 400 });
        }

        const timestamp = data.timestamp || new Date().toISOString();
        console.log(`[CONTACT] ${name} <${email}>: ${message}`);

        if (env.INQUIRIES) {
          await env.INQUIRIES.put(`inquiry:${Date.now()}:${email}`, JSON.stringify(data));
        } else if (env.GTC_DATA) {
          await env.GTC_DATA.put(`inquiry:${Date.now()}:${email}`, JSON.stringify(data));
        }

        if (env.CONTACT_WEBHOOK_URL) {
          try {
            await fetch(env.CONTACT_WEBHOOK_URL, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(data)
            });
          } catch(e) {}
        }

        if (env.RESEND_API_KEY) {
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
          } catch(e) {}
        }

        return Response.json({ success: true, message: 'Message sent successfully' });
      } catch (err) {
        return Response.json({ error: 'Failed to process inquiry' }, { status: 500 });
      }
    }

    // 4. Default: Serve Static Assets
    if (env.ASSETS) {
      return env.ASSETS.fetch(request);
    }

    return new Response('Not found', { status: 404 });
  }
};
