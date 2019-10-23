#!/bin/bash

echo "checking system performance"

IS_CPU_OK()
{
   echo "Printing CPU OUTPUT"
   uptime
}
IS_MEMORY_FINE()
{
   echo "PRINTING MEMORY PERFORMANCE"
   vmstat 5 10 # MEMORy performace 10 times at 5 seconds gap.
}
TOP_PERFORMANCE()
{
   echo "PRINTING TOP PERFORMANCE"
   top
}
IS_CPU_OK
IS_MEMORY_FINE
TOP_PERFORMANCE

exit 0




