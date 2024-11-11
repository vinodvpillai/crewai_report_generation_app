# Crewai-Report-Generation-App

A streamlined application built with **CrewAI** for generating reports using intelligent agent orchestration. This repository includes configurations for agents and tasks, crew management logic, and a main entry point for passing user queries. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

![](https://github.com/vinodvpillai/crewai_report_generation_app/blob/master/resources/output.gif)
## Project Structure

The repository consists of the following key files:

```bash
crewai-report-generation-app
├── .gitignore Specifies files and directories to ignore in Git
├── pyproject.toml   Project configuration and dependencies
├── README.md  Project documentation
├── .env Environment variables
└── src/ Source code directory
    └── my_project/  Main application package
        ├── __init__.py Marks the directory as a Python package
        ├── main.py  Main application script
        ├── crew.py  Crew-related functionalities
        ├── tools/   Custom tools directory
        │ ├── custom_tool.py  Custom tool implementation
        │ └── __init__.py  Marks tools directory as a package
        └── config/  Configuration files directory
            ├── agents.yaml   Agent configurations
            └── tasks.yaml Task configurations
```

## Installation

EEnsure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

> **Note**: Make sure to include `CrewAI` and any other required libraries in `requirements.txt`.

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

## How to Use

1. **Setup Configuration**:
   - Customize `agents.yaml` to define agent roles, goals, and backgrounds.
   - Update `tasks.yaml` for specifying task descriptions, tools, and expected outputs.

2. **Run the Application**:
   To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

   ```bash
   crewai run
   ```

3. **Review the Output**:
   The generated report will be displayed in the console or saved to a specified output file as defined in the `crew.py` logic.
   This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Project Overview

This application leverages **CrewAI's** capabilities for coordinating agents with distinct goals and tasks to generate reports efficiently. Each component plays a critical role:

- **Agents**: Specialized roles described in `agents.yaml` facilitate tailored responses and problem-solving approaches.
- **Tasks**: Configured in `tasks.yaml`, ensuring agents perform structured actions with clear expected results.
- **Crew Logic**: `crew.py` handles agent orchestration, defining how tasks are distributed and processed.
- **Main Script**: `main.py` initiates the process and connects user inputs with the CrewAI framework.

## Features

- **Configurable Agents**: Modify agent characteristics and roles as needed.
- **Flexible Task Descriptions**: Adjust task specifics for different report types.
- **Simple Integration**: Use `main.py` to easily pass queries and trigger the workflow.
- **Scalable Logic**: Expandable to include more agents and complex tasks as your use case grows.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.
