from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def get_instance(id, collection):
        return [x for x in collection if x.id == id][0]

    def edit_category(self, category_id: int, new_name: str):
        category = Storage.get_instance(category_id, self.categories)
        return category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = Storage.get_instance(topic_id, self.topics)
        return topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = Storage.get_instance(document_id, self.documents)
        return document.edit(new_file_name)

    def delete_category(self, category_id):
        category = Storage.get_instance(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = Storage.get_instance(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = Storage.get_instance(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = Storage.get_instance(document_id, self.documents)
        return repr(document)

    def __repr__(self):
        return "\n".join([repr(document) for document in self.documents])
