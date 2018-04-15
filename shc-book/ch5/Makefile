all: basicheap unlink_exploit unlink_exploit_dbg shrinking_free_chunks shrinking_free_chunks_dbg house_of_spirit house_of_spirit_dbg house_of_lore house_of_lore_dbg house_of_force house_of_force_dbg house_of_einherjar house_of_einherjar_dbg

basicheap:
	gcc -o basicheap basicheap.c

unlink_exploit:
	gcc -o unlink_exploit unlink_exploit.c

unlink_exploit_dbg:
	gcc -g -o unlink_exploit_dbg unlink_exploit.c

shrinking_free_chunks:
	gcc -o shrinking_free_chunks shrinking_free_chunks.c

shrinking_free_chunks_dbg:
	gcc -g -o shrinking_free_chunks_dbg shrinking_free_chunks.c

house_of_spirit:
	gcc -o house_of_spirit house_of_spirit.c

house_of_spirit_dbg:
	gcc -g -o house_of_spirit_dbg house_of_spirit.c

house_of_lore:
	gcc -o house_of_lore house_of_lore.c

house_of_lore_dbg:
	gcc -g -o house_of_lore_dbg house_of_lore.c

house_of_force:
	gcc -o house_of_force house_of_force.c

house_of_force_dbg:
	gcc -g -o house_of_force_dbg house_of_force.c

house_of_einherjar:
	gcc -o house_of_einherjar house_of_einherjar.c

house_of_einherjar_dbg:
	gcc -g -o house_of_einherjar_dbg house_of_einherjar.c

clean:
	rm basicheap unlink_exploit unlink_exploit_dbg shrinking_free_chunks shrinking_free_chunks_dbg house_of_spirit house_of_spirit_dbg house_of_lore house_of_lore_dbg house_of_force house_of_force_dbg house_of_einherjar house_of_einherjar_dbg


.PHONY: clean all
