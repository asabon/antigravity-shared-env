param(
    [Parameter(Mandatory=$true)]
    [int]$PrNumber
)

Write-Host "--- PR #$PrNumber Automated Verification ---" -ForegroundColor Cyan

# 1. PR Info
$prJson = gh pr view $PrNumber --json labels,body | ConvertFrom-Json

if (-not $prJson) {
    Write-Error "Failed to get PR #$PrNumber info."
    exit 1
}

$hasError = $false

# 2. Verify Labels
if ($prJson.labels.Count -eq 0) {
    Write-Host "[FAIL] No labels found on PR." -ForegroundColor Red
    $hasError = $true
} else {
    Write-Host "[OK] Labels found or added." -ForegroundColor Green
}

# 3. Verify Unchecked Checkboxes
# Match "- [ ]" in body
if ($prJson.body -match "- \[ \]") {
    Write-Host "[FAIL] Unchecked checkboxes found in PR body." -ForegroundColor Red
    $hasError = $true
} else {
    Write-Host "[OK] All checkboxes are completed." -ForegroundColor Green
}

# 4. Verify Linked Issue
if ($prJson.body -match '(?i)closes\s+#(\d+)') {
    $issueNum = $Matches[1]
    Write-Host "Found linked issue: #$issueNum" -ForegroundColor Cyan
    
    $issueJson = gh issue view $issueNum --json body | ConvertFrom-Json
    if ($issueJson) {
        if ($issueJson.body -match "- \[ \]") {
            Write-Host "[FAIL] Unchecked checkboxes found in linked issue #$issueNum body." -ForegroundColor Red
            $hasError = $true
        } else {
            Write-Host "[OK] Linked issue #$issueNum is all checked." -ForegroundColor Green
        }
    } else {
        Write-Host "[WARNING] Could not retrieve body for issue #$issueNum." -ForegroundColor Yellow
    }
} else {
    Write-Host "[OK] No linked issue found or matched ('Closes #XX')." -ForegroundColor Green
}

Write-Host "----------------------------------"

if ($hasError) {
    Write-Host "[RESULT] Verification FAILED!" -ForegroundColor Yellow
    exit 1
} else {
    Write-Host "[RESULT] Verification PASSED!" -ForegroundColor Green
    exit 0
}
