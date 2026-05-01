import re
from pathlib import Path

text = Path('yao-tutorial-skill.md').read_text(encoding='utf-8')
tutorial = Path('tutorial.md').read_text(encoding='utf-8')

checks = {
    'has_workflow': all(k in text for k in ['核心流程','多格式导出','质量验证']),
    'has_output_spec': all(k in text for k in ['brief.json','tutorial.md','exports/tutorial.pdf']),
    'tutorial_beginner_friendly': all(k in tutorial for k in ['目标读者','问题驱动','Checklist']),
    'tutorial_engineering_depth': all(k in tutorial for k in ['七层 Harness 模型','质量门禁','反模式']),
    'tutorial_has_actionability': bool(re.search(r'make run|run -> eval -> report', tutorial)),
}

score = sum(checks.values()) / len(checks) * 100
print('checks=', checks)
print(f'score={score:.1f}')
