"""OpenSEO 成本情景计算（基于仓库 README 与 src/shared/rank-tracking.ts 的公开常量）。"""
from decimal import Decimal, ROUND_HALF_UP

# 排名跟踪：queued SERP，depth=50：0.0006 + 4*0.00045 = 0.0024 USD / keyword check。
queued_depth50 = Decimal('0.0006') + Decimal(4) * Decimal('0.00045')
weekly_100 = queued_depth50 * Decimal(100) * Decimal(4)  # 近似 4 周/月

# 站点审计：仓库默认 maxPages=50，auto Lighthouse=20；OnPage crawl 与 Lighthouse 均视为 DataForSEO 用量。
# DataForSEO Lighthouse 的实际单价需以官网为准；这里用变量化估算，避免把未验证价格写死为事实。
site_audit_placeholder_low = Decimal('0')
semrush_user_baseline = Decimal('129')
semrush_current_pro = Decimal('139.95')

print(f"queued_depth50_per_keyword_check_usd={queued_depth50}")
print(f"rank_tracking_100_keywords_weekly_approx_month_usd={weekly_100.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
print(f"user_requested_semrush_baseline_usd={semrush_user_baseline}")
print(f"current_observed_semrush_pro_monthly_usd={semrush_current_pro}")
print(f"rank_tracking_vs_129_ratio={(weekly_100 / semrush_user_baseline * 100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}%")
