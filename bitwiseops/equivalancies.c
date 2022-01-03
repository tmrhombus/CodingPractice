/* Equivalent bitwise and logical operator tests */
#include <stdio.h>

void testOperator(char* name, unsigned char was, unsigned char expected);

int main( void )
{
   // -- Bitwise operators -- //

   //Truth tables packed in bits
   const unsigned char operand1    = 0x0A; //0000 1010
   const unsigned char operand2    = 0x0C; //0000 1100
   const unsigned char expectedAnd = 0x08; //0000 1000
   const unsigned char expectedOr  = 0x0E; //0000 1110
   const unsigned char expectedXor = 0x06; //0000 0110
	
   const unsigned char operand3    = 0x01; //0000 0001
   const unsigned char expectedNot = 0xFE; //1111 1110

   testOperator("Bitwise AND", operand1 & operand2, expectedAnd);
   testOperator("Bitwise  OR", operand1 | operand2, expectedOr);
   testOperator("Bitwise XOR", operand1 ^ operand2, expectedXor);
   testOperator("Bitwise NOT", ~operand3, expectedNot);	
   printf("\n");

   // -- Logical operators -- //

   const unsigned char F = 0x00; //Zero
   const unsigned char T = 0x01; //Any nonzero value

   // Truth tables packed in arrays

   const unsigned char operandArray1[4]    = {T, F, T, F};
   const unsigned char operandArray2[4]    = {T, T, F, F};
   const unsigned char expectedArrayAnd[4] = {T, F, F, F};
   const unsigned char expectedArrayOr[4]  = {T, T, T, F};
   const unsigned char expectedArrayXor[4] = {F, T, T, F};
	
   const unsigned char operandArray3[2]    = {F, T};
   const unsigned char expectedArrayNot[2] = {T, F};

   int i;
   for (i = 0; i < 4; i++)
   {
      testOperator("Logical AND", operandArray1[i] && operandArray2[i], expectedArrayAnd[i]);
   }
   printf("\n");

   for (i = 0; i < 4; i++)
   {
      testOperator("Logical  OR", operandArray1[i] || operandArray2[i], expectedArrayOr[i]);
   }
   printf("\n");

   for (i = 0; i < 4; i++)
   {
      //Needs ! on operand's in case nonzero values are different
      testOperator("Logical XOR", !operandArray1[i] != !operandArray2[i], expectedArrayXor[i]);
   }
   printf("\n");

   for (i = 0; i < 2; i++)
   {
      testOperator("Logical NOT", !operandArray3[i], expectedArrayNot[i]);
   }
   printf("\n");

   return 0;
}

void testOperator( char* name, unsigned char was, unsigned char expected )
{
   char* result = (was == expected) ? "passed" : "failed";
   printf("%s %s, was: %X expected: %X \n", name, result, was, expected);    
}
