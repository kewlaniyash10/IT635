CREATE TABLE REPORTS (
	IssueID INT,
	ip_address VARCHAR(20),
	email VARCHAR(50) NOT NULL,
	PRIMARY KEY (IssueID),
	FOREIGN KEY (email) REFERENCES HR (hr_email),
	FOREIGN KEY (email) REFERENCES FINANCE (f_email),
	FOREIGN KEY (ip_address) REFERENCES HR (hr_ip),
	FOREIGN KEY (ip_address) REFERENCES FINANCE (f_ip)
);