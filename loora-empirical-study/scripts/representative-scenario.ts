/** Copy this file to a Loora checkout root, then run: bun representative-scenario.ts */
import { applyTransaction } from './packages/canvas/src/engine'
import { createCanvasDocument } from './packages/canvas/src/model'
import { compileCanvas, compileStandaloneHtml, compileReactComponent } from './packages/canvas/src/export'
import { createPageInputSchema, createPageTransaction, semanticTree } from './packages/agent/src/canvas-tools'

const source = createCanvasDocument('R&D security review', 'scenario')
const input = createPageInputSchema.parse({
  name: 'Deployment approval',
  children: [{ ref: 'cta', type: 'frame', name: 'Approve deployment', semanticTag: 'button',
    children: [{ type: 'text', name: 'Label', text: 'Approve deployment' }] }],
})
const created = createPageTransaction(source, input)
const document = applyTransaction(source, created.transaction).document
const options = { rootId: created.pageId }
const compiled = compileCanvas(document, options)
const result = {
  nodeCount: Object.keys(document.nodes).length,
  fragmentBytes: Buffer.byteLength(compiled.html + compiled.css + compiled.runtime),
  tree: semanticTree(document, created.pageId, 3),
  htmlBytes: Buffer.byteLength(compileStandaloneHtml(document, options)),
  reactBytes: Buffer.byteLength(compileReactComponent(document, options)),
}
console.log(JSON.stringify(result, null, 2))
if (result.nodeCount !== 3 || result.htmlBytes < 100 || result.reactBytes < 100) process.exit(1)
