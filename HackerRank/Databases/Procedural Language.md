Which one of the following is a procedural language ?

Domain relational calculus  
Tuple relational calculus  
Relational algebra  
Query language (*)

Aside:

[SQL Procedural Language](http://www.oracle.com/technetwork/products/rdb/sql-proc-lang-feat-334044.html)

- Compound statements
    - The familiar BEGIN ... END construct
- Declaration statements
    - DECLARE variables
    - DECLARE LOCAL TEMPORARY TABLE for temporary in-memory tables.
    - Rdb7.1 adds global variables which can be reference by all routines in the module and hold persistent data across call statements.
- Conditional statements
    - IF ... THEN ... ELSE
    - CASE ... WHEN ... END CASE
    - Rdb7.1 adds enhancements to the CASE statement allowing lists of value expressions, and a new searched form of the CASE statement.
- Looping statements
    - LOOP ... END LOOP
    - WHILE ... DO ... END WHILE
    - REPEAT ... UNTIL ... END REPEAT (Rdb7.1)
    - The counted loop FOR ... IN ... END FOR (Rdb7.1)
- Row processing
    - The cursor loop FOR ... SELECT ... DO ... END FOR
    - UPDATE ... WHERE CURRENT OF … statement
    - DELETE ... WHERE CURRENT OF ... statement
- Loop termination control statements
    - LEAVE
    - ITERATE (Rdb7.1)
- Table operations
    - Singleton SELECT statement
    - INSERT statement
    - INSERT ... SELECT statement
    - UPDATE statement
- Transaction statements
    - SET TRANSACTION
    - COMMIT
    - ROLLBACK
    - LOCK TABLE (Rdb7.1)
- Informational statement
    - GET DIAGNOSTICS
- Nested stored procedures
    - CALL statement
    - References to SQL functions
- Miscellaneous statements
    - RETURN: Return a SQL function result.
    - TRACE: Trace procedure parameters, variables.