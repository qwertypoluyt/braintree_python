#import braintree.transaction

class PagedCollection(object):
    def __init__(self, query, collection, klass, klass_name):
        self.current_page_number = collection["current_page_number"]
        self.items = [klass(item) for item in collection[klass_name]]
        self.klass = klass
        self.page_size = collection["page_size"]
        self.query = query
        self.total_items = collection["total_items"]

    def next_page(self):
        if self.is_last_page:
            return None
        return self.klass.search(self.query, self.current_page_number + 1)

    @property
    def current_page_size(self):
        if self.is_last_page:
            return self.total_items % self.page_size
        else:
            return self.page_size

    @property
    def is_last_page(self):
        return self.current_page_number == self.total_pages

    @property
    def total_pages(self):
        total_pages = self.total_items / self.page_size
        if self.total_items % self.page_size != 0:
            total_pages += 1
        return total_pages

    def __getitem__(self, index):
        return self.items[index]