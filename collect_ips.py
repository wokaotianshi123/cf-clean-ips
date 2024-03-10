name: Update IP List

on:
  schedule:
    - cron: '0 */6 * * *' # 每6小时运行一次
  workflow_dispatch: # 允许手动触发
  push: # 允许提交触发

jobs:

  update-ip-list:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
      
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install requests
        pip install beautifulsoup4
        
    - name: Run Python script
      run: |
        import os
        os.environ['QT_QPA_PLATFORM']='offscreen'
        python collect_ips.py
        
    - name: Commit and push changes
      run: |
        git config --global user.email "chenhua.xu@qq.com"
        git config --global user.name "wokaotianshi123"
        git add ip.txt
        git commit -m "Update IP list"
        git push
