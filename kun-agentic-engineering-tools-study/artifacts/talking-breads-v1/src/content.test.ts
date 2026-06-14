import { describe, expect, it } from 'vitest';import { siteContent } from './content';
describe('Talking Breads content model',()=>{it('has 8+ menu highlights in one editable data file',()=>{expect(siteContent.menu.length).toBeGreaterThanOrEqual(8)});it('does not present online ordering as live',()=>{expect(siteContent.notice.toLowerCase()).toContain('no online ordering')});});
