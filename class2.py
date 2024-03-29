class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag, 0) + 1

    def __getitems__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitems__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        iter(self.tags)


cloud = TagCloud()
# cloud["python"] = 10
len(cloud)
cloud.add('Python')
cloud.add("python")
cloud.add("python")
print(cloud.tags)
