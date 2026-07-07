import { render } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { Badge } from "@/components/ui/badge";

describe("Badge", () => {
  it("renders the badge data-slot contract", () => {
    const { container } = render(<Badge>Active</Badge>);

    const badge = container.querySelector('[data-slot="badge"]');

    expect(badge?.textContent).toBe("Active");
  });

  it("preserves custom className", () => {
    const { container } = render(<Badge className="custom-badge">Beta</Badge>);

    const badge = container.querySelector('[data-slot="badge"]');

    expect(badge?.className).toContain("custom-badge");
  });
});