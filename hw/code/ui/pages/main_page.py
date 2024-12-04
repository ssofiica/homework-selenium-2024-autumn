from ui.pages.base_page import BasePage
from ui.pages.audience import AudiencePage

class MainPage(BasePage):
    url = "https://ads.vk.com/hq/audience"

    def go_to_audience_page(self):
        # self.click(self.locators.PEOPLE_PAGE_LINK)
        return AudiencePage(self.driver)
    
    # def go_to_leadform_page(self):
    #     # self.click(self.locators.PEOPLE_PAGE_LINK)
    #     return LeadformPage(self.driver)

    # def go_to_company_page(self):
    #     # self.click(self.locators.PEOPLE_PAGE_LINK)
    #     return CompanyPage(self.driver)
    