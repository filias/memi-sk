#!/usr/bin/env bash
# Run on the existing memi.click server (Caddy + uv + memi user already set up).
# Usage: WEBHOOK_SECRET=xxxx bash setup.sh
set -euo pipefail

: "${WEBHOOK_SECRET:?Set WEBHOOK_SECRET (the GitHub webhook secret) before running}"

REPO=https://github.com/filias/memi-sk.git
APP_DIR=/opt/memi-sk

git clone "$REPO" "$APP_DIR"
chown -R memi:memi "$APP_DIR"

cd "$APP_DIR"
sudo -u memi uv sync

cp deploy/memi-sk.service /etc/systemd/system/memi-sk.service

echo "WEBHOOK_SECRET=${WEBHOOK_SECRET}" > /etc/memi-sk-webhook.env
chmod 600 /etc/memi-sk-webhook.env
cp deploy/memi-sk-webhook.service /etc/systemd/system/memi-sk-webhook.service

systemctl daemon-reload
systemctl enable --now memi-sk memi-sk-webhook

cat >> /etc/caddy/Caddyfile <<'EOF'

sk.memi.click {
    handle /deploy {
        reverse_proxy localhost:9005
    }
    handle {
        reverse_proxy localhost:8087
    }
}
EOF
systemctl reload caddy

echo ""
echo "Done."
echo "1. DNS A record for sk.memi.click -> this server."
echo "2. GitHub webhook at https://github.com/filias/memi-sk/settings/hooks"
echo "   URL: https://sk.memi.click/deploy   secret: \$WEBHOOK_SECRET   event: push"
