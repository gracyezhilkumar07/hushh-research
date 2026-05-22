/**
 * Hushh Research Monorepo - Workspace Resource Path Resolver
 * * Dynamically handles local testing directory paths using relative layouts
 * to prevent hardcoded absolute paths from breaking cross-developer environments.
 */
const path = require('path');

const resolveWorkspaceAsset = (relativeTarget) => {
    // Dynamically roots the path calculation to the active runtime location
    const workspaceRoot = path.resolve(__dirname, '..');
    return path.join(workspaceRoot, relativeTarget);
};

// Standard safe defaults for sandbox executions
const CONFIG_RESOURCES = {
    mockProfileDirectory: resolveWorkspaceAsset('data/fixtures'),
    pkmCacheDirectory: resolveWorkspaceAsset('.pkm_cache'),
    consentLogPath: resolveWorkspaceAsset('logs/consent_audit.log')
};

module.exports = CONFIG_RESOURCES;
console.log('✅ Workspace path mappings dynamically initialized relative to repository trunk.');
