# simple_firewall
Implements a primitive firewall simulator

I tested my program by generating dummy csv rule files populated with varying amounts of rule lines from 100 to 1 million and running normal testing for all the components.
I had initially thought to implement it via a prefix trie as this matched closely with a problem I encountered previously, then shifted to normal tree and finally ended up using dictionary.

The program returns a true or false if a rule is hit or not. It does not return the rule id. Also there are no exception handling written assuming that the input is never malformed as given.
Would have added statistics information like the number of rules processed, no of rules hit and no of rules miss and also a logger with varied debug levels if I had more time.

I am interested in working for platform team. The team description closely matches my interest and also given my prior experience designing system services and deployment, it would be a perfect fit for me.
