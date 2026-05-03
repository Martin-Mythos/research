// 伪代码：前端渲染层按角色隐藏字段（仍需后端二次裁剪）
import policy from './field-visibility.policy.json';

type Role = 'project_coordinator' | 'manufacturer_reporter' | 'reviewer' | 'demo_observer';

export function renderField(role: Role, key: string, value: unknown) {
  const deny = new Set(policy.roles[role].denyFields);
  if (deny.has(key)) return null;
  return <Row label={key} value={String(value ?? '')} />;
}
