
class Page():
    def __init__(self,page_data={
                                    'page':'page_data',
                                }):
        self.page_data = page_data

    def set(self,page):
        return self.page_data.get(page,'/=/ Page Erro /=/ Out Of Range')

if __name__=="__main__":
    page = Page()
    page.page_data['page_add'] = 'page_data_add'
    print(page.set('page_add'))