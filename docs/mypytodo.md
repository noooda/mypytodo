```yaml
1:
  title: sample1
  limit: yyyy-mm-dd
  status: in progress
  description: hogehogehogehogehogehogehogehoge
2:
  title: sample2
  limit: yyyy-mm-dd
  status: not started 
  description: fugafugafugafugafugafugafugafuga 
3:
  title: sample3
  limit: yyyy-mm-dd
  status: completed 
  description: hogehogehogehogehogehogehogehoge
4:
  title: sample4
  limit: yyyy-mm-dd
  status: paused 
  description: fugafugafugafugafugafugafugafuga 
```

1. Show tasks
    ```bash
    python main.py list
    ```
    - Load .yaml and display tasks in a formatted way.
    - 


argparse  
- just pass commands to CommandHandler
- extract commands from cli input

CommandHandler  
- has dictionary that map commands to methods
- dynamic method resolution would be more useful than dictionary
