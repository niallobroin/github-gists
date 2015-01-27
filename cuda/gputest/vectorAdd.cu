#include <stdio.h>

/* Code given to Niall OByrnes by Zedong Wu from the KAUST SWAG
*/



// Variables
float* h_A;
float* h_B;
float* h_C;
float* d_A;
float* d_B;
float* d_C;
bool noprompt = false;

// Functions
void CleanupResources(void);
void RandomInit(float*, int);
void ParseArguments(int, char**);

// Device code
__global__ void VecAdd(const float* A, const float* B, float* C, int N)
{
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < N)
        C[i] = A[i] + B[i];
}
int main(int argc, char** argv)
{

    printf("Vector Addition\n");
    int N = 5000;
    size_t size = N * sizeof(float);
    h_A = (float*)malloc(size);
    h_B = (float*)malloc(size);
    h_C = (float*)malloc(size);
    RandomInit(h_A, N);
    RandomInit(h_B, N);
    ( cudaMalloc((void**)&d_A, size) );
    ( cudaMalloc((void**)&d_B, size) );
    ( cudaMalloc((void**)&d_C, size) );
    ( cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice) );
    ( cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice) );
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
    VecAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N);
    ( cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost) );
    int i;
    double real=0.0;
    double error=0.0;
    for (i = 0; i < N; ++i) 
    {
	real+=pow(h_A[i]+h_B[i],2);
        error+=pow(h_A[i]+h_B[i]-h_C[i],2);
    }
    error=sqrt(error/real);
    if(error<1e-4)
    printf("passed with the error=%e\n",error);
    else
    printf("fail\n");
}
// Allocates an array with random float entries.
void RandomInit(float* data, int n)
{
    for (int i = 0; i < n; ++i)
        data[i] = rand() / (float)RAND_MAX;
}
