/**
 * Cloudflare Pages / Worker Function: /api/subscribe
 * Handles newsletter & mailing list subscriptions.
 */
export async function onRequestPost(context) {
  const { request, env } = context;

  try {
    const data = await request.json();
    const email = data.email ? String(data.email).trim() : '';

    if (!email || !email.includes('@')) {
      return new Response(JSON.stringify({ error: 'Valid email is required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const timestamp = data.timestamp || new Date().toISOString();
    console.log(`[NEWSLETTER_SUBSCRIBER] email: ${email}, time: ${timestamp}`);

    // 1. If Cloudflare KV is bound (e.g. env.SUBSCRIBERS or env.GTC_DATA)
    if (env && env.SUBSCRIBERS) {
      await env.SUBSCRIBERS.put(`sub:${Date.now()}:${email}`, JSON.stringify({ email, timestamp }));
    } else if (env && env.GTC_DATA) {
      await env.GTC_DATA.put(`sub:${Date.now()}:${email}`, JSON.stringify({ email, timestamp }));
    }

    // 2. If a webhook URL is configured in env (e.g. Zapier, Make, Slack, Discord, Google Sheet)
    if (env && env.NEWSLETTER_WEBHOOK_URL) {
      try {
        await fetch(env.NEWSLETTER_WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, timestamp, source: 'Good Therapy Colorado Website' })
        });
      } catch (webhookErr) {
        console.error('Webhook error:', webhookErr);
      }
    }

    return new Response(JSON.stringify({
      success: true,
      message: 'Successfully subscribed to Good Therapy Colorado mailing list!'
    }), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });
  } catch (err) {
    console.error('Subscription error:', err);
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
