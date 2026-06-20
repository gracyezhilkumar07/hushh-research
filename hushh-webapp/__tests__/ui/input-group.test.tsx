import { render } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import {
  InputGroup,
  InputGroupAddon,
  InputGroupInput,
  InputGroupTextarea,
} from "@/components/ui/input-group";

describe("InputGroup", () => {
  it("renders group and addon data-slot contracts", () => {
    const { container } = render(
      <InputGroup>
        <InputGroupAddon>https://</InputGroupAddon>
        <InputGroupInput aria-label="Website" />
      </InputGroup>,
    );

    expect(container.querySelector('[data-slot="input-group"]')).toBeTruthy();
    expect(container.querySelector('[data-slot="input-group-addon"]')).toBeTruthy();
    expect(container.querySelector('[data-slot="input-group-control"]')).toBeTruthy();
  });

  it("renders textarea control with input-group-control data-slot", () => {
    const { container } = render(
      <InputGroup>
        <InputGroupTextarea aria-label="Message" />
      </InputGroup>,
    );

    expect(
      container.querySelector('textarea[data-slot="input-group-control"]'),
    ).toBeTruthy();
  });
});