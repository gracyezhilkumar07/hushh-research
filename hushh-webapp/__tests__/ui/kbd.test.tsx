import { render } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import { Kbd, KbdGroup } from "@/components/ui/kbd";

describe("Kbd", () => {
  it("renders kbd with data-slot='kbd'", () => {
    const { container } = render(<Kbd>Ctrl</Kbd>)
    expect(container.querySelector('[data-slot="kbd"]')).toBeTruthy();
  });

  it("renders kbd group with data-slot='kbd-group'", () => {
    const { container } = render(
      <KbdGroup>
        <Kbd>Ctrl</Kbd>
        <Kbd>Alt</Kbd>
      </KbdGroup>,
    );

    expect(container.querySelector('[data-slot="kbd-group"]')).toBeTruthy();
  });
});