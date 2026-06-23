#!/usr/bin/env bash
set -euo pipefail

echo "This script shows deployment commands. Run each section manually from the correct folder."
echo
echo "Deploy profile README:"
echo "cd profile-readme/leandroer && git init && git branch -M main && git remote add origin https://github.com/leandroer/leandroer.git && git add README.md && git commit -m 'Add professional GitHub profile README' && git push -u origin main"
echo
echo "Deploy Sentinel Analytics Rules:"
echo "cd Sentinel-Analytics-Rules && git init && git branch -M main && git remote add origin https://github.com/leandroer/Sentinel-Analytics-Rules.git && git add . && git commit -m 'Add Sentinel Analytics Rules starter framework' && git push -u origin main"
echo
echo "Deploy Sentinel Workbooks:"
echo "cd Sentinel-Workbooks && git init && git branch -M main && git remote add origin https://github.com/leandroer/Sentinel-Workbooks.git && git add . && git commit -m 'Add Sentinel Workbooks starter framework' && git push -u origin main"
