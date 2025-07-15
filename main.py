import traceback
import functions as fn
import data as dt


def main():
    # Setup logger
    log = fn.setup_log()
    log.info("🔹 Starting the File Organizer Process...")

    # 🔹 Step 1: Main Folder Processing
    try:
        log.info("🔹 Step 1: Starting the main folder processing...")
        zip_names = fn.step_1(dt.source_path, dt.dest_path)
        log.debug("✅ Step 1 Completed: Main folder processed successfully.")

        if not zip_names:
            log.critical("❌ No ZIP files were found to extract. Exiting process.")
            return

        # 🔹 Step 2: Assigning and Moving Files
        try:
            log.info("🔹 Step 2: Assigning and Moving Files...")
            for zip_name in zip_names:
                fn.step_2(dt.dest_path, zip_name)
            log.info("✅ Step 2 Completed: All files processed.")

            # 🔹 Step 3: Renaming Files Accordingly
            try:
                log.info("🔹 Step 3: Summarizing.")
                fn.step_3(dt.dest_path)
                log.info("✅ Step 3 Completed: All files renamed successfully.")

            except Exception as e:
                log.error(f"❌ Error in Step 3 while renaming files: {e}")
                log.error(traceback.format_exc())

        except Exception as e:
            log.error(f"❌ Error in Step 2 while categorizing files: {e}")
            log.error(traceback.format_exc())

    except Exception as e:
        log.error(f"❌ Error in Step 2 during folder processing: {e}")
        log.error(traceback.format_exc())


if __name__ == "__main__":
    main()

