from secret_key import gemini_api_key
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
import os

os.environ["GOOGLE_API_KEY"] = gemini_api_key

llm = GoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.6)



def generate_resturant_name_and_menu_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open restaurant for {cuisine} food.Suggest me only one classic name with two words"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_idea = PromptTemplate(
        input_variables=['restaurant_name'],
        template="suggest some menu items names for {restaurant_name}.Names should be seperated by comma"
    )

    company_idea_chain = LLMChain(llm=llm, prompt=prompt_template_idea, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, company_idea_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})

    return response

if __name__=="__main__":
    print(generate_resturant_name_and_menu_items("Indian"))