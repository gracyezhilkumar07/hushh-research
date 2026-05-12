import { useEffect } from "react";

export const usePageTracking = () => {
  useEffect(() => {
    console.log("Page viewed:", window.location.pathname);
  }, []);
};
