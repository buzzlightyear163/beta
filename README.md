# BETA ($BETA): own the beta of every runner.

En fil: `index.html` (CSS och JS inbakade) plus `og.png` och `fav.png`. Ingen build.

## Vad som är riktigt och vad som är larp

| Del | Status |
|---|---|
| Breakouts (graduations) | riktigt, pump.fun-strömmen via PumpPortal (gratis, ingen nyckel) |
| Beta-kartan | riktigt, DexScreener-sökning + strömmen. Fem lanes: meme, ticker, theme, look (bildlikhet via dHash), dev (bara coins som launchats medan sidan är öppen) |
| Poäng | riktigt, relation × flow × headroom. Filter: headroom > 1.5×, mcap ≥ $4k, aktivitet senaste 5 min, ålder > 60 s |
| Betas som spawnar | riktigt, nya launches som kopierar en färsk runner flaggas i loggen |
| Korgens priser och P&L | riktiga priser (DexScreener var 20:e s), men köpen är paper fills och märkta "sim" |
| Vault-köp och buyback | larp, beskrivs i fees och token |

Når sidan inte strömmen eller DexScreener (till exempel i en förhandsvisning) visar den demo-data som tydligt märks "preview".

## Fyll i CONFIG (överst i sista scriptet i index.html)

```js
const CONFIG = { ca:"", x:"", dexscreener:"", site:"", ... }
```

- `ca`: kontraktsadressen efter launch. Tom = "posted here and on X at launch", och köpknappen är avstängd.
- `x`: länk till X-kontot. Tom = knappen döljs.
- `site`: din domän, läggs till i "post on x"-texten från beta-kartan.

## Deploy

GitHub → Vercel: nytt repo med de tre filerna i roten, importera i Vercel, Framework "Other", ingen build command, output = roten.

## Kolla efter deploy

1. Typsnittet är JetBrains Mono (laddas från Google Fonts).
2. X-förhandsvisning: klistra in domänen i en post-draft, og.png ska synas.
3. Live-data: lampan i "03 · live" ska stå på "live · pump.fun", och beta-kartan ska säga "live data" (inte preview).
4. Testa kartan med en CA från en färsk graduation och med exemplen ($fartcoin, $wif).

## Grafik

`grafik/`: pfp.png (2000×2000), banner.png (3000×1000), launch.png (3200×1800). Objektet är ett pixel-β med tre glödande betor (`beta` i termkit.js). Status LIVE, ingen CA, ingen länk.
