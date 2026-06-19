import { readFileSync } from 'node:fs';
const src = readFileSync(new URL('../src/main.tsx', import.meta.url),'utf8') + readFileSync(new URL('../src/content.ts', import.meta.url),'utf8');
const required=['Talking Breads Tervuren','Open Google Maps','View menu','Student lunch offer','Allergy information','Opening hours','info@talkingbreads.be'];
const missing=required.filter(x=>!src.includes(x));
if(/Order now|Pay online|Delivery scheduling/i.test(src)) throw new Error('Found forbidden live ordering/payment affordance');
if(missing.length) throw new Error('Missing required content: '+missing.join(', '));
console.log('smoke passed: required V1 content present and forbidden affordances absent');
