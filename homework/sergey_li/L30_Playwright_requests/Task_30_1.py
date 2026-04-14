from playwright.sync_api import Page, expect, Route
import json


def test_catch_response(page: Page):
    def modify_response(route: Route):
        response = route.fetch()
        try:
            body = response.json()
            body_str = json.dumps(body, ensure_ascii=False)
            modified_str = body_str.replace("iPhone\xa017\xa0Pro", "яблокофон 17 про")

            route.fulfill(
                status=response.status,
                headers=dict(response.headers),
                body=modified_str,
            )
        except Exception as e:
            route.continue_()

    page.route("**digital-mat**", modify_response)

    page.goto("https://www.apple.com/shop/buy-iphone")
    page.wait_for_load_state("networkidle")

    page.locator("img[src*='iphone-card-40-17pro']").click()

    popup = page.locator("[role='dialog']").first
    popup.wait_for(state="visible", timeout=10000)

    expect(popup.get_by_role("heading").first).to_contain_text("яблокофон 17 про")
