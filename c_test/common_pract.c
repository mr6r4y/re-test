/** 
 *  C Programming: Common Practices
 *  URL: https://en.wikibooks.org/wiki/C_Programming/Common_practices 
 *
**/

#include <stdlib.h>


// Constructors and destructors
struct string {
    size_t size;
    char *data;
};

struct string *create_string(const char *initial) {
    assert (initial != NULL);
    struct string *new_string = malloc(sizeof(*new_string));
    if (new_string != NULL) {
        new_string->size = strlen(initial);
        new_string->data = strdup(initial);
    }
    return new_string;
}


void free_string(struct string *s) {
    assert (s != NULL);
    free(s->data);  ''/* free memory held by the structure */''
    free(s);        ''/* free the structure itself */''
}
// -----------------------------


int main()
{	
	// Multi-dimentional arrays
	int rows = 7;
	int (*multi_array)[5] = malloc(rows * sizeof(int[5]));

	#define w 5
	#define x 5
	#define y 5
	#define z 5

	int dim1[w];
	int dim2[w * x];
	int dim3[w * x * y];
	int dim4[w * x * y * z];

	int i=3, j=2, k=1, l=4;

	dim1[i];
	dim2[w * j + i];
	dim3[w * (x * i + j) * k];
	// Note that w*(x*(y*i+j)+k)+l is equal to w*x*y*i + w*x*j + w*k + l, but uses fewer operations 
	// (see Horner's Method)
	dim4[w * (x * (y * j + i) + k) + l];
}