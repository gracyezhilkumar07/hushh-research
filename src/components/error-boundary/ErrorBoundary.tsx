import React from "react";
import * as Sentry from "@sentry/react";

type Props = {
  children: React.ReactNode;
};

export default class ErrorBoundary extends React.Component<Props> {
  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    Sentry.captureException(error);
    console.error(error, errorInfo);
  }

  render() {
    return this.props.children;
  }
}
