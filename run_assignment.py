"""Run the notebook's code cells and show results in the terminal."""
import json
import os
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
os.environ.setdefault('MPLCONFIGDIR', str(ROOT / '.jupyter' / 'matplotlib'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def terminal_display(*objects, **kwargs):
    for obj in objects:
        print(obj.to_string(index=False) if hasattr(obj, 'to_string') else obj)
        print()


def main():
    notebook = json.loads((ROOT / 'sales_assignment.ipynb').read_text(encoding='utf-8'))
    namespace = {'__name__': '__main__'}
    step = 0
    with patch('IPython.display.display', terminal_display), patch.object(plt, 'show', lambda: None):
        for cell in notebook['cells']:
            if cell['cell_type'] != 'code':
                continue
            step += 1
            print(f'\n========== Step {step} ==========\n')
            source = cell['source']
            exec(compile(''.join(source) if isinstance(source, list) else source,
                         f'notebook_step_{step}', 'exec'), namespace)
    plt.close('all')
    print('\nSUCCESS: Both parts completed. CSV files and charts were regenerated.')


if __name__ == '__main__':
    main()
