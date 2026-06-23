# Deployment Commands

## 1. Deploy GitHub Profile README

Create a repository named exactly:

```text
leandroer
```

Then deploy:

```bash
cd profile-readme/leandroer

git init
git branch -M main
git remote add origin https://github.com/leandroer/leandroer.git

git add README.md
git commit -m "Add professional GitHub profile README"
git push -u origin main
```

If the repo already exists:

```bash
git remote set-url origin https://github.com/leandroer/leandroer.git
git push -u origin main --force
```

## 2. Deploy Sentinel Analytics Rules Repository

Create the repo:

```bash
gh repo create Sentinel-Analytics-Rules --public
```

Or create it manually at:

```text
https://github.com/new
```

Then deploy:

```bash
cd Sentinel-Analytics-Rules

git init
git branch -M main
git remote add origin https://github.com/leandroer/Sentinel-Analytics-Rules.git

git add .
git commit -m "Add Sentinel Analytics Rules starter framework"
git push -u origin main
```

If GitHub says fetch first and the repository is new:

```bash
git push -u origin main --force
```

## 3. Deploy Sentinel Workbooks Repository

Create the repo:

```bash
gh repo create Sentinel-Workbooks --public
```

Then deploy:

```bash
cd Sentinel-Workbooks

git init
git branch -M main
git remote add origin https://github.com/leandroer/Sentinel-Workbooks.git

git add .
git commit -m "Add Sentinel Workbooks starter framework"
git push -u origin main
```

## 4. Copy Standard Templates Into Existing Repositories

For each existing repo:

```bash
cp repo-templates/DETECTION-DOCUMENTATION-TEMPLATE.md <repo>/docs/
cp repo-templates/PROJECT-ROADMAP.md <repo>/ROADMAP.md
```

Then commit:

```bash
git add .
git commit -m "Add standard project documentation templates"
git push
```

## 5. Add Architecture Diagrams

Copy diagrams into your repos:

```bash
cp diagrams/ai-security-operations-architecture.md AI-Security-Incident-Response-Lab/docs/
cp diagrams/sentinel-soar-architecture.md IncidentResponse/docs/
cp diagrams/snort-detection-architecture.md Snort-Detection-Engineering-Lab/docs/
```

Then commit and push.

## GitHub Token Reminder

If GitHub asks for a password, paste a Personal Access Token, not your GitHub password.

## Recommended Repository Descriptions

### Sentinel-Analytics-Rules

```text
Professional Microsoft Sentinel analytics rules for Identity, Microsoft Purview, AI Security, Microsoft Agent 365, Defender XDR, and SOC detection engineering.
```

### Sentinel-Workbooks

```text
Microsoft Sentinel workbook concepts for SOC operations, incident response, AI Security, Microsoft Purview, and automation monitoring.
```

### leandroer Profile README

```text
Professional GitHub profile README for cybersecurity portfolio visibility.
```
