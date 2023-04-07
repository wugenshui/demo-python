from steamship import Steamship

# Create a Steamship client
# NOTE: When developing a package, just use `self.client`
client = Steamship(workspace="gpt-4-um0p3")

# Create an instance of this generator
generator = client.use_plugin('gpt-4')

question = input("请输入你的问题:")

# Generate text
task = generator.generate(text=question)

# Wait for completion of the task.
task.wait()

# Print the output
print(task.output.blocks[0].text)
