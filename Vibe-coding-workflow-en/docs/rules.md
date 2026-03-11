# Coding Rules

## Default Rules
- Keep a layered design when applicable, such as interface, service, and data access layers. Do not pile business logic into entry files.
- Keep configuration in a dedicated place such as a config module or config file. Avoid scattered hard-coded values.
- Critical flows must have explicit error handling. Do not fail silently.
- Validate external input before entering business logic.
- Keep functions single-purpose. Split complex functions into smaller ones.
- Confirm scope before changing code, and provide at least minimal reproducible validation after the change.

## Naming
- Use meaningful names. Do not let names like `tmp` or `test1` enter production code.

## Style
- Keep formatting consistent and prefer small, low-coupling functions.

## Error Handling
- Error messages should be actionable and include enough context for diagnosis.

## Logging And Comments
- Log key paths. Comments should explain why, not restate what the code does.

## Security And Privacy
- Never commit secrets, tokens, passwords, or similar sensitive data.

## Testing And Regression
- Cover at least the main flow and one failure branch.

## Anti-Patterns
- Avoid direct cross-layer calls that create uncontrolled coupling.