"""Execute the notebook locally and save observed reference outputs."""
import contextlib
import io
import json
import os
import shutil
import tempfile
from pathlib import Path
root = Path(__file__).resolve().parents[1]
path = root/'notebooks'/'murshid.ipynb'
notebook = json.loads(path.read_text())
ns = {}
with tempfile.TemporaryDirectory() as temp:
    previous = Path.cwd()
    os.chdir(temp)
    try:
        for index, cell in enumerate(notebook['cells'], 1):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                exec(compile(''.join(cell['source']), f'cell-{index}', 'exec'), ns)
            cell['execution_count'] = index
            cell['outputs'] = []
            if output.getvalue():
                cell['outputs'].append({'output_type':'stream','name':'stdout','text':output.getvalue().splitlines(keepends=True)})
        for filename in ('baseline_results.json','day2_results.json','day3_results.json','day4_results.json','final_report.json'):
            shutil.copy(Path('murshid_outputs')/filename, root/'expected'/filename)
        shutil.copy(Path('murshid_outputs')/'synthetic_data.json', root/'data'/'synthetic_data.json')
    finally:
        os.chdir(previous)
path.write_text(json.dumps(notebook,ensure_ascii=False,indent=2)+'\n')
print('Recorded locally observed outputs; no Google Colab session was used.')
