param (
    [string]$BranchName
)

if (-not $BranchName) {
    # Get current branch if no argument provided
    $BranchName = (git branch --show-current).Trim()
}

Write-Host "--- Verifying Branch Name: $BranchName ---"

# Expected format: <IssueNumber>-<description>
# Regex: ^\d+-[a-z0-9-]+$
if ($BranchName -notmatch '^\d+-[a-z0-9-]+$') {
    Write-Error "[FAIL] Branch name does not follow the naming convention (<IssueNumber>-description)"
    Write-Host "Expected: 123-feature-name"
    Write-Host "Current: $BranchName"
    exit 1
}

Write-Host "[OK] Branch name format is valid."
exit 0
