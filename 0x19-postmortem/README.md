![f](https://github.com/Mhjba/alx-system_engineering-devops/assets/132380677/3f028fc1-74b3-4d0c-9935-3422297f8fa1)

Issue Summary:

Date:
09/05/2024

Time:
The event started at 10:00 AM UTC and ends at 14:22 PM UTC .

Impact: 
The web server experienced intermittent downtime, affecting approximately 30% of users accessing the platform.

Root Cause: 
misconfiguration of web server's SSL certificate, causing SSL handshake failures.

Timeline:                                              
10:00 AM (UTC)
problem detected as users reported difficulty accessing the website.
10:15 AM
Initial verification began, focusing on server logs and network traffic.
11:00 AM
Monitoring systems identified SSL handshake failures as a significant problem.
11:30 AM
Engineering team started examining SSL certificate configuration.
12:00 PM
Misconfiguration was detected in the SSl certificate, leading to intermittent failures in SSL handshakes.
13:00 PM
Escalation to security team for further analysis and resolution.
13:30 PM
Reconfigured SSL certificate to resolve handshake failures.
14:22 PM
Normal service restored, web server functioning properly.

Root Cause and Resolution:
The root cause of the issue was a misconfiguration in the web server's SSL certificate, resulting in intermittent SSL handshake failures. These failures prevented users from establishing secure connections to the server, leading to downtime. The issue was resolved by correcting the SSL certificate configuration to ensure proper handshake procedures.

Corrective and Preventative Measures:
Implement automated SSL certificate monitoring and validation processes.
Developed automated scans to verify SSL certificate configurations and detect  misconfigurations promptly.
Enhance documentation and training for system administrators on SSL certificate management best practices.
Conduct regular audits of SSL certificate configurations to identify and rectify any deviations from standards.
Creating redundant SSL certificate configurations to reduce the impact of similar issues in the future.

Conclusion:
By implementing these corrective actions and improving our SSL certificate management practices, we aim to enhance the reliability and security of our web server infrastructure, reducing the likelihood of similar incidents  in the future.


