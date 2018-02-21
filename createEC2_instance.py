import configHeader
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
	description="This script creates an EC2 instance\n")

requiredNamed = parser.add_argument_group('Required arguments')

requiredNamed.add_argument('-a', metavar='ec2type', type=str, required=True, dest='ec2type',
		help='Ec2 api id for the instance which will be created\n')
requiredNamed.add_argument('-n', metavar='ec2name', required=True, dest='ec2name',
 		help='Ec2 name for the instance which will be created\n')

args = parser.parse_args()

def CreateInstance(ec2type,ec2name):
		key_pair = configHeader.ec2.create_key_pair(KeyName='TestKey.pem')
		KeyPairOut = str(key_pair.key_material)
		with open('TestKey.pem', 'w') as file:
				file.write(KeyPairOut)

		response = configHeader.ec2.create_instances(
			ImageId=ec2type,
			MinCount=1, MaxCount=1,
			KeyName="TestKey.pem",
			InstanceType="t2.micro"
		)
		configHeader.ec2.create_tags(Resources=[response[0].id], Tags=[{'Key':'Name', 'Value':ec2name}])
		print(response[0].id)

if __name__ == '__main__':
    CreateInstance(args.ec2type,args.ec2name)
