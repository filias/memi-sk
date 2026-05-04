# memi slovensko

A Slovak memory card game built on [memi-engine](https://github.com/filias/memi-engine).

Live at [sk.memi.click](https://sk.memi.click)

## Categories

- **Geografia: Kraje** — 8 administrative regions of Slovakia
- **Geografia: Mestá** — major Slovak cities
- **Geografia: Rieky** — main rivers of Slovakia
- **Kultúra: Pamiatky** — historic landmarks and monuments
- **Kultúra: Jedlá** — traditional Slovak dishes
- **Kultúra: Kluby** — Slovak top-flight football clubs
- **Príroda: Zvieratá** — native Slovak animals
- **Príroda: Rastliny** — native Slovak plants and trees
- **Ľudia** — historical and modern figures (by era)

## Setup

```bash
uv sync
uv run python -m memi_sk.app
```

## Deploy

Pushes to `main` auto-deploy via GitHub webhook.
