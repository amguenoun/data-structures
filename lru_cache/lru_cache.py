from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList() 
        self.cache = {} # key : node pointer

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache: #if key exists in cache returns value of node
            node = self.cache[key]
            self.storage.move_to_front(node)
            return node.value[1]
        else:
            return None #else returns none


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.cache: #Checks if key exists in cache and if yes
            node = self.cache[key] #grabs the node pointer
            self.storage.delete(node)  #removes node from position in DLL
            self.storage.add_to_head((key, value)) #adds node to head
            self.cache[key] = self.storage.head #updates the pointer in cache to head
        elif len(self.cache) >= self.limit: #Checks if cache is over limit, if yes
            self.cache.pop(self.storage.tail.value[0]) #removes last item from cache
            self.storage.remove_from_tail() #removed last node from DLL
            self.storage.add_to_head((key,value)) #adds new node to DLL
            self.cache[key] = self.storage.head #adds new item in cache pointing to new node
        else:
            self.size += 1 #updates size
            self.storage.add_to_head((key,value)) #adds new node to DLL
            self.cache[key] = self.storage.head #adds new pointer to cache
