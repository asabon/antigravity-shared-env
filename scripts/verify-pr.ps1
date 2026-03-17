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

Write-Host "----------------------------------"

if ($hasError) {
    Write-Host "[RESULT] Verification FAILED!" -ForegroundColor Yellow
    exit 1
} else {
    Write-Host "[RESULT] Verification PASSED!" -ForegroundColor Green
    exit 0
}
