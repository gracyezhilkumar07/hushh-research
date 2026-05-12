const requiredEnvVars = [
  "VITE_SENTRY_DSN",
];

requiredEnvVars.forEach((envVar) => {
  if (!import.meta.env[envVar]) {
    console.warn(`Missing environment variable: ${envVar}`);
  }
});
