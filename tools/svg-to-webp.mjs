// Convert assets/img/src/*.svg to WebP (quality 80). Run: node tools/svg-to-webp.mjs
// Needs sharp: `npm i -g sharp` or NODE_PATH pointing at a folder with sharp installed.
import { createRequire } from 'node:module';
import { readdirSync, statSync, renameSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const sharp = require(process.env.SHARP_PATH || 'sharp');
const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const src = join(root, 'assets/img/src');
const out = join(root, 'assets/img');

const special = {};
// Extra smaller widths for responsive srcset.
const extraWidths = { 'hero-mountains': [800], 'resin-drop': [480] };
const THUMB_SMALL = 400; // every thumb-*.svg also gets a 400px version

for (const f of readdirSync(src).filter((n) => n.endsWith('.svg'))) {
  const name = f.slice(0, -4);
  const dir = special[name] || out;
  const tasks = [[join(dir, `${name}.webp`), null]];
  for (const w of (extraWidths[name] || (name.startsWith('thumb-') ? [THUMB_SMALL] : []))) tasks.push([join(dir, `${name}-${w}.webp`), w]);
  for (const [file, w] of tasks) {
    let img = sharp(join(src, f), { density: 144 });
    const meta = await sharp(join(src, f)).metadata();
    img = img.resize({ width: w || meta.width });
    await img.webp({ quality: 80 }).toFile(file + '.tmp');
    renameSync(file + '.tmp', file);
    const kb = (statSync(file).size / 1024).toFixed(1);
    if (statSync(file).size > 120 * 1024) throw new Error(`${file} is ${kb} KB (> 120 KB)`);
    console.log(`${file.replace(root + '/', '')}  ${kb} KB`);
  }
}
