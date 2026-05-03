// 伪代码：将 open-design 生成的页面嵌入业务壳并接入 i18n
const locale = userPreference ?? 'en'; // 默认 EN
const bundles = {
  en: require('./en.json'),
  'zh-CN': require('./zh-CN.json')
};

export function t(key: string) {
  return bundles[locale]?.[key] ?? bundles.en[key] ?? key;
}

export function buildCaseTabs() {
  return [
    { id: 'group-b', label: t('case.groupB.title') },
    { id: 'group-d', label: 'Reporting Action' }
  ];
}
