# EC2 WorkWeek Scheduler (AWS Lambda)

This AWS Lambda function automatically starts and stops EC2 instances based on Indian Standard Time (IST) workweek hours. It ensures your instances run only from **9:00 AM to 9:00 PM IST (Monday to Friday)** and remain **stopped during off-hours and weekends**, saving costs.

---

## 💡 Use Case

Use this setup for:

- Developer or testing environments
- Cost-optimized automation for non-production workloads
- Automatically powering down during non-business hours

---

## ⏰ Scheduling Logic

| Day       | 9 AM - 9 PM | 9 PM - 9 AM |
|-----------|-------------|-------------|
| Mon–Fri   | EC2 Running | EC2 Stopped |
| Sat–Sun   | EC2 Stopped | EC2 Stopped |

---

## 🛠 How It Works

1. **Lambda is triggered** twice daily via Amazon EventBridge (CloudWatch).
2. **Time zone** is converted to IST using `pytz`.
3. EC2 instances are managed based on **tags**:
   - **Start logic**: Starts stopped instances with `AutoStart=true`.
   - **Stop logic**: Stops running instances with `AutoStop=true`.

---

## 🏷 Tagging Your EC2 Instances

To include EC2 instances in this schedule, tag them appropriately:

| Key         | Value   | Used For       |
|--------------|----------|----------------|
| `Environment`| Development | General grouping |
| `AutoStart`  | true     | To auto-start instances at 9 AM |
| `AutoStop`   | true     | To auto-stop instances at 9 PM |

### ✅ How to Tag Instances:

1. Go to **EC2 Console > Instances**.
2. Select the instance(s).
3. Click **Tags > Manage Tags**.
4. Add these tags:
   - `Environment = Development`
   - `AutoStart = true` *(for starting)*
   - `AutoStop = true` *(for stopping)*
5. Save the changes.

### Architecture 
![ChatGPT Image Apr 5, 2025, 07_45_13 AM](https://github.com/user-attachments/assets/706083f0-ce7c-4168-89d2-debb15074612)

 

 
