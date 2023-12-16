import time
class Controller:
    def __init__(self, client, assistant_id):
        self.assistant_id = assistant_id
        self.client = client
        self.my_assistant = self.client.beta.assistants.retrieve(assistant_id)
        self.thread = self.client.beta.threads.create()

    def query_gpt(self, query):
        """
        Sends the formatted query to the GPT model and returns the response.
        """
        try:
            message = self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=f"{query}"
            )
            run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id,
            )

            while run.status != "completed":
                run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id
                )
                time.sleep(1)

            messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id
            ) 

            return messages
        
        except Exception as e:
            print(e)
            return None

    def close_thread(self):
        """
        Closes the thread to free up resources.
        """
        self.client.beta.threads.delete(thread_id=self.thread.id)

class Proof_sketch_controller(Controller):

    '''A controller for proof sketch GPTs.
    Each initialization should start an individual thread, which we will append messages to.'''
    def __init__(self, client, assistant_id):
        super().__init__(client, assistant_id)

    def add_proof_examples(self, problem_description):
        """
        Find and add proof examples to the GPT query.
        """
        # Implement logic to add context to the problem description
        enhanced_query = problem_description  # Placeholder
        return enhanced_query

    def expand_proof(self, response):
        """
        Expand or clarify steps in the GPT-generated proof.
        """
        inferred_steps = response  # Placeholder
        return inferred_steps

    def validate_proof(self, proof_sketch):
        """
        Checks the coherence and validity of the proof sketch against known mathematical principles.
        """
        is_valid = True  # Placeholder
        return is_valid

    def generateProofSketch(self, problem_description):
        """
        Main method to generate a proof sketch for a given mathematical problem.
        """
        enhanced_query = self.enhanceQueryWithContext(problem_description)
        gpt_response = self.queryGPT(enhanced_query)
        if gpt_response:
            proof_with_inferred_steps = self.inferAdditionalSteps(gpt_response)
            if self.validateProof(proof_with_inferred_steps):
                return proof_with_inferred_steps
            else:
                return "Proof validation failed."
        else:
            return "Failed to generate proof sketch."

class Autoformalizer_controller(Controller):

    '''Controller for autoformalizer GPTs. Call for examples and translate from English to formal math.'''

    def __init__(self, client, assistant_id):
        super().__init__(client, assistant_id)

    def add_translation_examples(self, problem_description):
        """
        Adds translation examples to the GPT query.
        """
        # Implement logic to add translation examples to the problem description
        enhanced_query = problem_description  # Placeholder
        return enhanced_query
    



