import playwright.sync_api

class TestCases:
    def __init__(self, page: playwright.sync_api.Page):
        self.page = page

    def check_test_exist(self, test_name: str):
        return self.page.query_selector(f'css=tr >> text=\"{test_name}\"') is not None

    def delete_test_by_name(self, test_name: str):
        row = self.page.query_selector(f'*css=tr >> text=\"{test_name}\"')
        row.query_selector('.deteteBtn').click()

    def check_columns_hidden(self):
        description = self.page.is_hidden('.thDes')
        autor = self.page.is_hidden('.thAutor')
        executor = self.page.is_hidden('.thLast')
        return description and autor and executor